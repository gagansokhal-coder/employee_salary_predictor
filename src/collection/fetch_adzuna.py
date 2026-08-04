"""
==========================================================
Adzuna Dataset Collector
Author : Gagan
Version : 1.0
==========================================================
"""

import os
import json
import time
import random
import logging
from pathlib import Path
from datetime import datetime

import pandas as pd
import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from config import (
    APP_ID,
    APP_KEY,
    COUNTRIES,
    KEYWORDS,
    START_PAGE,
    END_PAGE,
    REQUEST_DELAY,
    MAX_RETRIES,
    RATE_LIMIT_WAIT,
    SERVER_ERROR_WAIT,
    CONNECTION_WAIT,
    TIMEOUT_WAIT,
    REQUEST_TIMEOUT,
)

# ==========================================================
# Create folders automatically
# ==========================================================

RAW_DATA_DIR = Path("data/raw")
LOG_DIR = Path("data/logs")

RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

CHECKPOINT_DIR = Path("checkpoint")

CHECKPOINT_DIR.mkdir(exist_ok=True)

CHECKPOINT_FILE = CHECKPOINT_DIR / "checkpoint.json"

# ==========================================================
# Logging
# ==========================================================

logging.basicConfig(
    filename=LOG_DIR / "fetch.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)

# ==========================================================
# HTTP Session
# ==========================================================

session = requests.Session()

retry_strategy = Retry(
    total=0,            # we'll handle retries manually
    connect=0,
    read=0,
    status=0,
)

adapter = HTTPAdapter(max_retries=retry_strategy)

session.mount("http://", adapter)
session.mount("https://", adapter)

# ==========================================================
# Request Headers
# ==========================================================

HEADERS = {
    "User-Agent":
    (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )
}

# ==========================================================
# Checkpoint Functions
# ==========================================================

def load_checkpoint():

    default = {
        "country": None,
        "keyword": None,
        "page": START_PAGE
    }

    if not CHECKPOINT_FILE.exists():
        return default

    try:
        with open(CHECKPOINT_FILE, "r") as f:
            return json.load(f)

    except:
        return default


def save_checkpoint(country, keyword, page):
    """
    Save current progress.
    """

    checkpoint = {

    "country": country,

    "keyword": keyword,

    "page": page,

    "total_jobs": TOTAL_JOBS,

    "requests": TOTAL_REQUESTS,

    "success": SUCCESS_REQUESTS,

    "failed": FAILED_REQUESTS,

    "retries": TOTAL_RETRIES,

    "last_updated": str(datetime.now())

}

    with open(CHECKPOINT_FILE, "w") as f:

        json.dump(checkpoint, f, indent=4)

# ==========================================================
# Utility Functions
# ==========================================================

def save_jobs(country, jobs):
    """
    Append jobs into country CSV.
    """

    if len(jobs) == 0:
        return

    csv_path = RAW_DATA_DIR / f"{country}.csv"

    df = pd.DataFrame(jobs)

    if csv_path.exists():

        df.to_csv(
            csv_path,
            mode="a",
            header=False,
            index=False
        )

    else:

        df.to_csv(
            csv_path,
            index=False
        )


def random_delay():
    """
    Sleep randomly between requests.
    """

    delay = REQUEST_DELAY + random.uniform(0.2, 0.8)

    time.sleep(delay)


def print_progress(
        country,
        keyword,
        page,
        fetched,
        total_jobs,
        start_time
):

    elapsed = time.time() - start_time
    total_pages = len(COUNTRIES) * len(KEYWORDS) * END_PAGE

    completed = TOTAL_REQUESTS

    eta = (elapsed / completed) * (total_pages-completed) if completed else 0

    print(

    f"ETA : {time.strftime('%H:%M:%S', time.gmtime(eta))}"

)

    jobs_per_min = total_jobs / (elapsed / 60)

    requests_per_min = TOTAL_REQUESTS / (elapsed / 60)

    print()

    print("=" * 80)

    print(f"Country            : {country.upper()}")

    print(f"Keyword            : {keyword}")

    print(f"Page               : {page}")

    print(f"Jobs This Page     : {fetched}")

    print(f"Total Jobs         : {total_jobs:,}")

    print(f"Requests           : {TOTAL_REQUESTS}")

    print(f"Successful         : {SUCCESS_REQUESTS}")

    print(f"Failed             : {FAILED_REQUESTS}")

    print(f"Retries            : {TOTAL_RETRIES}")

    print(f"Duplicates Removed : {DUPLICATE_JOBS}")

    print(f"Jobs / Minute      : {jobs_per_min:.1f}")

    print(f"Requests / Minute  : {requests_per_min:.1f}")

    print(f"Elapsed            : {time.strftime('%H:%M:%S', time.gmtime(elapsed))}")

    print("=" * 80)

# ==========================================================
# Startup Information
# ==========================================================

checkpoint = load_checkpoint()

TOTAL_JOBS = 0
# ==========================================================
# Statistics
# ==========================================================

TOTAL_REQUESTS = 0

SUCCESS_REQUESTS = 0

FAILED_REQUESTS = 0

TOTAL_RETRIES = 0

DUPLICATE_JOBS = 0

COUNTRY_JOB_COUNT = {}

# Already seen IDs
SEEN_IDS = set()
def load_existing_ids(country):

    csv_path = RAW_DATA_DIR / f"{country}.csv"

    if not csv_path.exists():
        return

    try:

        temp = pd.read_csv(csv_path, usecols=["id"])

        SEEN_IDS.update(temp["id"].tolist())

        print(f"Loaded {len(SEEN_IDS):,} existing IDs")

    except Exception:

        pass

START_TIME = time.time()

print()

print("=" * 70)

print("Adzuna Dataset Collector Started")

print(f"Started at : {datetime.now()}")

print(f"Countries  : {len(COUNTRIES)}")

print(f"Keywords   : {len(KEYWORDS)}")

print(f"Pages      : {START_PAGE} -> {END_PAGE}")

print("=" * 70)

logger.info("Crawler Started")
# ==========================================================
# Production Request Function
# ==========================================================

def fetch_page(url, params, country, keyword, page):
    """
    Fetch one page from Adzuna API.

    Returns
    -------
    jobs : list
        List of jobs if successful.

    None
        If page should be skipped.
    """

    retries = 0
    global TOTAL_REQUESTS
    global SUCCESS_REQUESTS
    global FAILED_REQUESTS
    global TOTAL_RETRIES

    while retries < MAX_RETRIES:

        try:
            

            TOTAL_REQUESTS += 1

            response = session.get(

                url,

                headers=HEADERS,

                params=params,

                timeout=REQUEST_TIMEOUT

            )

            status = response.status_code

            # ==========================================
            # SUCCESS
            # ==========================================

            if status == 200:
                

                SUCCESS_REQUESTS += 1

                try:

                    data = response.json()

                except ValueError:

                    print(
                        f"[JSON ERROR] "
                        f"{country} | "
                        f"{keyword} | "
                        f"Page {page}"
                    )

                    logger.warning("JSON Decode Error")

                    retries += 1
                   
                    TOTAL_RETRIES += 1

                    time.sleep(5)

                    continue

                return data.get("results", [])

            # ==========================================
            # BAD REQUEST
            # ==========================================

            elif status == 400:
               
                FAILED_REQUESTS += 1

                print(

                    f"[400] Bad Request "

                    f"{country} "

                    f"{keyword}"

                )

                logger.error("400 Bad Request")

                return None

            # ==========================================
            # UNAUTHORIZED
            # ==========================================

            elif status == 401:

                print(

                    "\n401 Unauthorized"

                    "\nCheck APP_ID / APP_KEY"

                )

                logger.error("401 Unauthorized")

                raise SystemExit

            # ==========================================
            # FORBIDDEN
            # ==========================================

            elif status == 403:

                print(

                    "\n403 Forbidden"

                )

                logger.error("403 Forbidden")

                retries += 1
               
                TOTAL_RETRIES += 1

                time.sleep(60)

                continue

            # ==========================================
            # NOT FOUND
            # ==========================================

            elif status == 404:

                print(

                    f"404 Not Found "

                    f"{country}"

                )

                logger.warning("404")
                
                FAILED_REQUESTS += 1

                return None

            # ==========================================
            # TOO MANY REQUESTS
            # ==========================================

            elif status == 429:

                retries += 1
               
                TOTAL_RETRIES += 1

                wait = RATE_LIMIT_WAIT + random.randint(5,25)

                print()

                print("="*60)

                print("429 RATE LIMIT")

                print(f"Retry : {retries}/{MAX_RETRIES}")

                print(f"Waiting {wait} sec")

                print("="*60)

                logger.warning("429 Rate Limit")

                time.sleep(wait)

                continue

            # ==========================================
            # SERVER ERRORS
            # ==========================================

            elif status in [500,502,503,504]:

                retries += 1
               
                TOTAL_RETRIES += 1

                wait = SERVER_ERROR_WAIT + random.randint(5,20)

                print()

                print("="*60)

                print(

                    f"{status} Server Error"

                )

                print(

                    f"Retry : {retries}/{MAX_RETRIES}"

                )

                print(

                    f"Waiting {wait} sec"

                )

                print("="*60)

                logger.warning(

                    f"{status}"

                )

                time.sleep(wait)

                continue

            # ==========================================
            # OTHER STATUS
            # ==========================================

            else:

                print(

                    f"Unhandled Status : {status}"

                )

                logger.warning(status)
                
                FAILED_REQUESTS += 1

                return None

        # ==========================================
        # INTERNET LOST
        # ==========================================

        except requests.exceptions.ConnectionError:

            retries += 1
           
            TOTAL_RETRIES += 1

            print()

            print("="*60)

            print("Connection Lost")

            print(f"Retry : {retries}")

            print(f"Waiting {CONNECTION_WAIT}")

            print("="*60)

            logger.warning("Connection Error")

            time.sleep(CONNECTION_WAIT)

        # ==========================================
        # TIMEOUT
        # ==========================================

        except requests.exceptions.Timeout:

            retries += 1
          
            TOTAL_RETRIES += 1

            print()

            print("="*60)

            print("Request Timed Out")

            print(f"Retry : {retries}")

            print(f"Waiting {TIMEOUT_WAIT}")

            print("="*60)

            logger.warning("Timeout")

            time.sleep(TIMEOUT_WAIT)

        # ==========================================
        # CTRL + C
        # ==========================================

        except KeyboardInterrupt:

            print()

            print("Stopping... Saving Checkpoint")

            save_checkpoint(

                country,

                keyword,

                page

            )

            logger.info("Interrupted")

            raise SystemExit

        # ==========================================
        # UNKNOWN
        # ==========================================

        except Exception as e:

            retries += 1
           
            TOTAL_RETRIES += 1

            print()

            print(e)

            logger.exception(e)

            time.sleep(30)

    print()

    print("="*60)

    print("Maximum retries reached")

    print(country)

    print(keyword)

    print(page)

    print("="*60)

    logger.error(

        "Maximum Retry"

    )
    
    FAILED_REQUESTS += 1

    return None

# ==========================================================
# Main Crawling Loop
# ==========================================================

resume = checkpoint["country"] is not None

for country in COUNTRIES:

    # Skip countries until checkpoint is reached
    if resume and country != checkpoint["country"]:
        continue

    print(f"\n{'='*80}")
    print(f"Starting Country : {country.upper()}")
    print(f"{'='*80}")

    logger.info(f"Starting Country : {country}")
    load_existing_ids(country)

    # csv_file = RAW_DATA_DIR / f"{country}.csv"

    country_jobs = 0

    for keyword in KEYWORDS:

        # Resume keyword
        if resume and keyword != checkpoint["keyword"]:
            continue

        print(f"\nKeyword : {keyword}")

        logger.info(f"Keyword : {keyword}")

        start_page = START_PAGE

        # Resume page
        if resume:
            start_page = checkpoint["page"]
            resume = False

        for page in range(start_page, END_PAGE + 1):

            save_checkpoint(country, keyword, page)

            url = (
                f"https://api.adzuna.com/v1/api/jobs/"
                f"{country}/search/{page}"
            )

            params = {

                "app_id": APP_ID,

                "app_key": APP_KEY,

                "what": keyword,

                "results_per_page": 50,

                "sort_by": "date"

            }

            # -------------------------------------
            # Actual Request
            # (Retry logic comes in Part-3)
            # -------------------------------------

            jobs = fetch_page(

                  url=url,

                  params=params,

                 country=country,

                 keyword=keyword,

                  page=page

            )

            if jobs is None:

                continue

            # -------------------------------------
            # No Jobs
            # -------------------------------------

            if len(jobs) == 0:

                print(
                    f"No jobs found after Page {page} "
                    f"-> Skipping remaining pages."
                )

                logger.info(
                    f"No jobs | "
                    f"{country} | "
                    f"{keyword} | "
                    f"{page}"
                )

                break

            # -------------------------------------
            # Save Immediately
            # -------------------------------------

          
            filtered_jobs = []
            for job in jobs:

                  job_id = job.get("id")

                  if job_id in SEEN_IDS:

                     DUPLICATE_JOBS += 1

                     continue

                  SEEN_IDS.add(job_id)

                  filtered_jobs.append(job)

            save_jobs(country, filtered_jobs)
            save_checkpoint(

              country,

              keyword,

                 page + 1

        )

            fetched = len(filtered_jobs)

            TOTAL_JOBS += fetched

            country_jobs += fetched

            # -------------------------------------
            # Console Output
            # -------------------------------------

            print_progress(

                country=country,

                keyword=keyword,

                page=page,

                fetched=fetched,

                total_jobs=TOTAL_JOBS,

                start_time=START_TIME

            )

            logger.info(

                f"{country} | "
                f"{keyword} | "
                f"Page {page} | "
                f"{fetched}"

            )

            random_delay()

    print()

    print(f"Finished Country : {country.upper()}")

    print(f"Country Jobs     : {country_jobs:,}")
    COUNTRY_JOB_COUNT[country] = country_jobs
    logger.info(

        f"Finished {country} | Jobs : {country_jobs}"

    )
    csv_path = RAW_DATA_DIR / f"{country}.csv"

    try:

        temp = pd.read_csv(csv_path)

        before = len(temp)

        temp.drop_duplicates(subset=["id"], inplace=True)

        after = len(temp)

        temp.to_csv(csv_path, index=False)

        print(
        f"Removed {before-after} duplicate rows."
     )

    except Exception as e:

        print(e)

elapsed = time.time() - START_TIME

print()

print("=" * 80)

print("FETCH COMPLETED")

print("=" * 80)

print(f"Countries Processed : {len(COUNTRIES)}")

print(f"Keywords            : {len(KEYWORDS)}")

print(f"Total Requests      : {TOTAL_REQUESTS:,}")

print(f"Successful          : {SUCCESS_REQUESTS:,}")

print(f"Failed              : {FAILED_REQUESTS:,}")

print(f"Retries             : {TOTAL_RETRIES:,}")

print(f"Duplicates Removed  : {DUPLICATE_JOBS:,}")

print(f"Jobs Collected      : {TOTAL_JOBS:,}")

print(f"Elapsed             : {time.strftime('%H:%M:%S', time.gmtime(elapsed))}")

print("=" * 80)

logger.info("Crawler Finished Successfully")