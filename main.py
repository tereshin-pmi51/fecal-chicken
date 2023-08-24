from cnnClassifier import logger
from cnnClassifier.pipeline.stge_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f'>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(
        f'>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<<<\n\n\nxxxxxxxxxxxxxxxxxxxxxxxxxx')
except Exception as e:
    logger.exception(e)
    raise e