from rest_framework import serializers
from .models import Artist

# class RiskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Risk
#         fields = ('id', 'title',)
#
# class ActionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Actions
#         fields = ('id', 'title',)

class musicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('artist', 'album', 'track_name')

    # def to_representation(self, instance):
    #     response_dict = dict()
    #     response_dict[instance.artist] = {
    #         'album': AlbumSerializer(instance.album.all(), many=True).data,
    #         'track_name': TrackNameSerializer(instance.track_name.all(), many=True).data
    #     }
    #     return response_dict
