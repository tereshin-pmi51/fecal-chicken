from cnnClassifier.config.configuration import ConfigurationManconager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

STAGE_NAME = "Data ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        configMGR = ConfigurationManconager()
        data_ingestion_config = configMGR.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        logger.info(f'>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<<<')
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<<<\n\n\nxxxxxxxxxxxxxxxxxxxxxxxxxx')
    except Exception as e:
        logger.exception(e)
        raise e
