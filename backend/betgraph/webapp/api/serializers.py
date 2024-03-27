from rest_framework import serializers


class BetSerializer(serializers.Serializer):
    person_id = serializers.UUIDField(read_only=True)
    username = serializers.CharField()
    gender = serializers.CharField()


class PersonSerializer(serializers.Serializer):
    person_id = serializers.UUIDField(read_only=True)
    username = serializers.CharField()
    gender = serializers.CharField(required=False, allow_null=True)
    bets = BetSerializer(many=True)
    answered = serializers.DateTimeField(required=False, allow_null=True)
    timestamp = serializers.DateTimeField()
