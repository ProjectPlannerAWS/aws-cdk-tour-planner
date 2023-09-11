import aws_cdk as core
import aws_cdk.assertions as assertions

from src.aws_cdk_tour_planner_stack import AwsCdkTourPlannerStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_cdk_tour_planner/aws_cdk_tour_planner_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCdkTourPlannerStack(app, "aws-cdk-tour-planner")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
