from src.user_interaction import UserInteractionHH, UserInteractionJson


request_user = UserInteractionHH()
request_user.user_request()

answer_user = UserInteractionJson()
answer_user.json_request()
