from rest_framework import generics, viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User,RasPi, UserBottle, Container, ContainerImage
from .serializers import UserSerializer, RasPiSerializer, UserBottleSerializer

class UserBottleViewSet(viewsets.ModelViewSet):
    queryset = UserBottle.objects.all()
    serializer_class = UserBottleSerializer

    # user_idを渡す
    @action(detail=False, methods=['post'])
    def bottle_list(self, request):
        user_bottle = UserBottle.objects.filter(user_id=request.data["user_id"])
        # serializer = self.get_serializer(user_bottle, many=True)  FavoriteSerializerがなかったら、get_serialiozerで行ける
        serializer = UserBottleSerializer(user_bottle, many=True)
        response = {"data": serializer.data}
        return Response(response)

    # 新規のデータを渡す
    @action(detail=False, methods=['post'])
    def new_bottle(self, request):
        serializer = self.UserBottleSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    # 更新情報を渡す
    @action(detail=False, methods=['post'])
    def update_bottle(self, request):
        bottle_info = UserBottle.objects.get(id=request.data["id"])
        serializer = UserBottleSerializer(bottle_info, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save(owner=request.user)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def update_quantity(self, request):
        raspi = RasPi.objects.get(individual_id=request.data["raspi_id"])
        user_bottle = UserBottle.objects.get(raspi_id_id=raspi.id)
        serializer = UserBottleSerializer(user_bottle, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save(owner=request.user)
        return Response(serializer.data)

    # idとis_favoriteを渡す
    # @action(detail=False, methods=['post'])
    # def is_favorite(self, request):
    #     is_favorite = BottleInformation.queryset.get(id=request.data["id"])
    #     serializer = BottleInformationSerializer(is_favorite, fields=(request.data['id'], request.data['is_favorite']))
    #     serializer.is_valid()
    #     serializer.save(owner=request.user)
    #     return Response(serializer.data)



# class Favorite(viewsets.ModelViewSet):
#     queryset = BottleInformation.objects.all()
#     serializer_class = FavoriteSerializer



    # @action(detail=False, methods=['post'])
    # def favorite(self, request):
    #     bottle_info = BottleInformation.queryset.get(id=request.data["id"])
    #     serializer = BottleInformationSerializer()
    #     serializer.is_valid()
    #     serializer.save(is_favorite=request.data["is_favorite"])
    #     return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def user_info(self, request):
        user_info = User.objects.get(id=request.data["id"])
        serializer = self.get_serializer(user_info)
        response = {"data": serializer.data}
        # return Response(serializer.data)
        return Response(response)

    # @action(detail=False, methods=['post'])
    # def new_user

    @action(detail=False, methods=['post'])
    def user_update(self, request):
        user_info = User.objects.get(id=request.data["id"])
        serializer = UserSerializer(user_info, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save(owner=request.user)


class RasPiViewSet(viewsets.ModelViewSet):
    queryset = RasPi.objects.all()
    serializer_class = RasPiSerializer

    @action(detail=False, methods=['post'])
    def rasp_info(self, request):
        rasp_info = RasPi.objects.filter(individual_id=request.data["individual_id"])
        serializer = self.get_serializer(rasp_info, many=True)
        return Response(serializer.data)

    # @action(detail=False, methods=['post'])
    # def new_bottle(self, request):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid()
    #     serializer.save()
    #     return Response(serializer.data)