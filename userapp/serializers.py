from pickletools import read_long1
from .models import UserProfile, Post
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = UserProfile
        fields = ['user','profile_pic', 'dob', 'full_name', 
        'Section', 'Branch', 'year_joined', 
        'Hosteler_or_DayScholar', 'Hostel_Room_No', 
        'bio', 'Native_Language', 'Languages_Known', 
        'Address', 'State', 'foreigners_can_enter_their_states_here', 
        'Country', 'whatsapp', 'instagram_username',
         'facebook', 'linkdin_profile_link', 'gmail']
    def validate(self, data):
            data['user'] = self.context['request'].user
            return data


class UserPostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields = ['id','author' ,'title', 'image', 'description', 'created', 'updated']
    def validate(self, data):
            data['author'] = self.context['request'].user
            return data
    
    