"""API module"""

import time

import requests

from tuinbouwer_sensor import BASE_URL, HEADERS, LOGGER


def post_sensor_log(sensor_log):
    """Download item id"""
    tries = 1
    while tries <= 3:
        try:
            response = requests.post(
                '{}{}'.format(BASE_URL, 'sensor_api/v1/'),
                headers=HEADERS,
                json=sensor_log,
            )
            if response:
                return response.json()
        except requests.exceptions.ConnectionError as error:
            LOGGER.error(error)
            LOGGER.info("Connection error while POST sensor log")
        except requests.exceptions.MissingSchema as error:
            LOGGER.error(error)
            LOGGER.info("Something is wrong with the URL")
        except Exception as error:
            LOGGER.info("Something wrong with API request")
            LOGGER.info(error)
        LOGGER.info("Trying again to POST sensor log")
        time.sleep(5)
        tries += 1
