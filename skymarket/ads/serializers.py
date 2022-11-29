from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from users.models import User
from users.serializers import CurrentUserSerializer
from ads.models import Comment, Ad


class CommentSerializer(serializers.ModelSerializer):
    author = CurrentUserSerializer()
    class Meta:
        model = Comment
        fields = '__all__'


class AdCreateSerializer(serializers.ModelSerializer):
    author = CurrentUserSerializer(read_only=True)

    class Meta:
        model = Ad
        fields = ['pk', 'title', 'price', 'image', 'description', 'author']

# class AdSerializer(serializers.ModelSerializer):
#     first_name = SlugRelatedField(slug_field="first_name", queryset=User.objects.all())
#     # last_name = SlugRelatedField(slug_field="last_name", queryset=User.objects.all())
#     # phone = SlugRelatedField(slug_field="phone", queryset=User.objects.all())
#     # author_id = SlugRelatedField(slug_field="phone", queryset=User.objects.all())
#
#     class Meta:
#         model = Ad
#         fields = ['title', 'price', 'image', 'description', 'first_name']


class AdSerializer(serializers.ModelSerializer):
    # author = CurrentUserSerializer()

    class Meta:
        model = Ad
        fields = ['pk', 'title', 'price', 'image', 'description', 'author']

class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.SerializerMethodField()

    def get_author_first_name(self, ad):
        return ad.author.first_name

    def get_author_last_name(self, ad):
        return ad.author.last_name

    class Meta:
        model = Ad
        fields = ['pk', 'title', 'price', 'image', 'description', 'author']