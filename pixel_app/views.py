from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from .models import *
# from jwt_auth.models import *
from .serializers.common import *

# Create your views here.

#! PIXEL VIEWS

class ListView(ListAPIView):
  queryset = Pixel.objects.all()
  serializer_class = PopulatedPixelSerializer

class CreateView(CreateAPIView):
  queryset = Pixel.objects.all()
  serializer_class = PixelSerializer

class DetailView(RetrieveAPIView):
  queryset = Pixel.objects.all()
  serializer_class = PopulatedPixelSerializer

class UpdateDeletePixel(APIView):
  # def get(self, request, pk):
  #        # Call the get_author function which will either get the author or raise a HTTP 404 status code response if not present
  #       owner = self.get_author(pk=pk)

  #       # Create a new serializer with the current author data - we're only returning one author so we don't need the many=True flag
  #       serialized_author = AuthorSerializer(author)

  #        # Return the serialized author data and a HTTP 200 response
  #       return Response(data=serialized_author.data, status=status.HTTP_200_OK)
  def put(self, request, pk):
    # pixel_to_update =self.get_pixel(pk=pk)
    pixel_to_update = Pixel.objects.get(pk=pk)
    request.data['current_owner'] = request.user.id
    pixel_serializer = PixelSerializer(pixel_to_update, data=request.data)
    
    if pixel_serializer.is_valid():
      pixel_serializer.save()
      return Response(data= pixel_serializer.data, status= status.HTTP_200_OK)
    return Response(data=pixel_serializer.errors, status= status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    pixel_to_delete = self.get_pixel(pk=pk)
    pixel_to_delete.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  def get_pixel(self, pk):
    try:
      return Pixel.objects.get(pk=pk)
    except Pixel.DoesNotExist:
      raise NotFound(detail="Can't find that pixel")


#! COLOR VIEWS

class ListColorView(ListAPIView):
  queryset = Color.objects.all()
  serializer_class = ColorSerializer

class CreateColorView(CreateAPIView):
  queryset = Color.objects.all()
  serializer_class = ColorSerializer

class ColorDetailView(RetrieveUpdateDestroyAPIView):
  queryset = Color.objects.all()
  serializer_class = ColorSerializer


#! Owner Serializer

class ListOwnerView(ListAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = OwnerSerializer

class DetailOwnerView(RetrieveUpdateDestroyAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = OwnerSerializer

#! Thread Views

class ListThreadsView(ListAPIView):
  queryset = Thread.objects.all()
  serializer_class = PopulatedThreadSerializer

class DetailThreadView(RetrieveDestroyAPIView):
  queryset = Thread.objects.all()
  serializer_class = PopulatedThreadSerializer

class UpdateThreadView(APIView):
  permission_classes = [IsAuthenticated,]
  def put(self, request, pk):
      thread_to_update = Thread.objects.get(pk=pk)
      if (thread_to_update.id != request.user.id):
        return Response(status=status.HTTP_403_FORBIDDEN)
      
      thread_serializer = ThreadSerializer(thread_to_update, data=request.data)
      if thread_serializer.is_valid():
          thread_serializer.save()

          # Return on the response
          return Response(data=thread_serializer.data, status=status.HTTP_200_OK)

      return Response(data=thread_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateThreadView(CreateAPIView):
  queryset = Thread.objects.all()
  serializer_class = ThreadSerializer


#! Community Views

class ListCommunityView(ListAPIView):
  queryset=Community.objects.all()
  serializer_class = CommunityWithCreatorSerializer

class DetailCommunityView(RetrieveDestroyAPIView):
  queryset = Community.objects.all()
  serializer_class = CommunityWithCreatorSerializer

class UpdateCommunityView(APIView):
  permission_classes = [IsAuthenticated,]
  def put(self, request, pk):
      community_to_update = Community.objects.get(pk=pk)
      if (community_to_update.creator.id != request.user.id):
        return Response(status=status.HTTP_403_FORBIDDEN)
      
      community_serializer = CommunitySerializer(community_to_update, data=request.data)
      if community_serializer.is_valid():
          community_serializer.save()

          # Return on the response
          return Response(data=community_serializer.data, status=status.HTTP_200_OK)

      return Response(data=community_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateCommunityView(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self, request):

        request.data['creator'] = request.user.id
        community_serializer = CommunitySerializer(data=request.data)
        if community_serializer.is_valid():
            community_serializer.save()

            # Get newly created community ID
            new_community_id = community_serializer.data['id']

            # Load the community back out of the database
            new_community = Community.objects.get(pk=new_community_id)

            # Serialize it using the CommunityWithOwnerSerializer
            community_with_owner_serializer = CommunityWithCreatorSerializer(new_community)

            # Return on the response
            return Response(data=community_with_owner_serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=community_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#! Comment Views

class ListCommentView(ListAPIView):
  queryset=Comment.objects.all()
  serializer_class = PopulatedCommentSerializer

class DetailCommentView(RetrieveDestroyAPIView):
  queryset = Comment.objects.all()
  serializer_class = PopulatedCommentSerializer

class CreateCommentView(APIView):
  permission_classes = [IsAuthenticated,]
  def post(self, request):


        request.data['creator_of_comment'] = request.user.id
        comment_serializer = CommentSerializer(data=request.data)
        if comment_serializer.is_valid():
            comment_serializer.save()

            # Get newly created community ID
            new_comment_id = comment_serializer.data['id']

            # Load the community back out of the database
            new_comment = Comment.objects.get(pk=new_comment_id)

            # Serialize it using the CommunityWithOwnerSerializer
            comment_with_owner_serializer = PopulatedCommentSerializer(new_comment)

            # Return on the response
            return Response(data=comment_with_owner_serializer.data, status=status.HTTP_201_CREATED)



        return Response(data=comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateCommentView(APIView):

  permission_classes = [IsAuthenticated,]
  def put(self, request, pk):
        comment_to_update = Comment.objects.get(pk=pk)
        print ('comment id', comment_to_update.creator_of_comment.id)
        print ('request id: ', request.user.id)
        if (comment_to_update.creator_of_comment.id != request.user.id):
          return Response(status=status.HTTP_403_FORBIDDEN)
        
        comment_serializer = CommentSerializer(comment_to_update, data=request.data)
        if comment_serializer.is_valid():
            comment_serializer.save()

            # Return on the response
            return Response(data=comment_serializer.data, status=status.HTTP_200_OK)

        return Response(data=comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)