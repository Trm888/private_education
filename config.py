import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from loguru import logger

load_dotenv()

if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()
    print(ROOT_DIR)
else:
    ROOT_DIR = Path(__file__).parent.absolute()
    print(ROOT_DIR)

FILES_DIR = os.path.join(ROOT_DIR, 'files')
ABIS_DIR = os.path.join(ROOT_DIR, 'data', 'abis')
logger.success(ABIS_DIR)
DEBUG_LOG = os.path.join(FILES_DIR, 'debug.log')
print(DEBUG_LOG)

logger.add(f'{DEBUG_LOG}', format='{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}', level='DEBUG', rotation="1000 KB",
           compression='zip')
# logger.remove()

ETHEREUM_API_KEY = str(os.getenv('ETHEREUM_API_KEY'))
ARBITRUM_API_KEY = str(os.getenv('ARBITRUM_API_KEY'))
OPTIMISM_API_KEY = str(os.getenv('OPTIMISM_API_KEY'))
BSC_API_KEY = str(os.getenv('BSC_API_KEY'))
POLYGON_API_KEY = str(os.getenv('POLYGON_API_KEY'))
AVALANCHE_API_KEY = str(os.getenv('AVALANCHE_API_KEY'))
MOONBEAM_API_KEY = str(os.getenv('MOONBEAM_API_KEY'))
FANTOM_API_KEY = str(os.getenv('FANTOM_API_KEY'))
CELO_API_KEY = str(os.getenv('CELO_API_KEY'))
GNOSIS_API_KEY = str(os.getenv('GNOSIS_API_KEY'))
HECO_API_KEY = str(os.getenv('HECO_API_KEY'))
GOERLI_API_KEY = str(os.getenv('GOERLI_API_KEY'))
SEPOLIA_API_KEY = str(os.getenv('SEPOLIA_API_KEY'))


def divide(a, b):
    return a / b


@logger.catch
def main():
    divide(1, 0)


if __name__ == '__main__':
    main()
