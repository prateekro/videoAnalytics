# import os
# from google.cloud import videointelligence
#
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="VideoAnalyticsEngine-c194ee79cbef.json"
#
# client = videointelligence.VideoIntelligenceServiceClient()
# job = client.annotate_video(
#     input_uri='gs://vision-bucket-store/phone.mp4',
#     features=['LABEL_DETECTION'], #, 'SHOT_CHANGE_DETECTION'
# )
# result = job.result()

