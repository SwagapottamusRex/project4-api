from rest_framework import serializers
from ..models import Color, Community, CustomUser, Pixel, Thread, Comment

class PixelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pixel
    fields = ('__all__')

class OwnerSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ('username', 'email', 'date_joined', 'image', )

class ColorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Color
    fields = ('__all__')


class PopulatedPixelSerializer(PixelSerializer):
  color = ColorSerializer(many=False)
  current_owner = OwnerSerializer(many=False)


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
      model = Community
      fields = ('__all__')

class CommunityWithCreatorSerializer(CommunitySerializer):
    creator = OwnerSerializer()


class ThreadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Thread
    fields = ('__all__')

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ('__all__')
    



class PopulatedCommentSerializer(CommentSerializer):
  creator_of_comment = OwnerSerializer()

# class PopulatedCommentSerializerCreate(CommentSerializer):
#   creator_of_comment = PopulatedCommentSerializer()



class PopulatedCommunitySerializer(CommunitySerializer):
  creator = OwnerSerializer()


class PopulatedThreadSerializer(ThreadSerializer):
  community = PopulatedCommunitySerializer(many=False)
  #! many = True bugging out!!!
  reply_thread = PopulatedCommentSerializer()

  # queryset = Comment.objects.all()
  # reply_thread = CommentSerializer(queryset, many=True)
  # serializer.data
