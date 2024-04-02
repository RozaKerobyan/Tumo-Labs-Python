class FbModel:
    def __init__(self, profile_picture, cover_picture):
        self.profile_picture = profile_picture
        self.cover_picture = cover_picture

    def get_profile_picture_url(self):
        return "www.fb.com/profile/"+self.profile_picture

    def get_cover_picture_url(self):
        return "www.fb.com/cover/"+self.cover_picture
    

class Profile(FbModel):
    
    def __init__(self,first_name, last_name, profile_picture=None, cover_picture=None):
        super().__init__(profile_picture, cover_picture)
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return self.first_name+" - "+self.last_name

class Page(FbModel):
    def __init__(self,name, profile_picture, cover_picture, followers=0):
        super().__init__(profile_picture, cover_picture)
        self.name = name
        self.followers = followers

    def get_info(self):
        return{
            'name':self.name,
            'followers':self.followers
        }

user1 = Profile(first_name="Roza", last_name="Kerobyan", profile_picture="roza.jpeg", cover_picture="roza_cover.jpeg")

KeRozPage = Page("KeRoz","keroz.jpeg","keroz_cover.jpeg")

print("========")
print(KeRozPage.get_profile_picture_url(), KeRozPage.get_cover_picture_url())
print("========")
print(user1.profile_picture, user1.cover_picture)
print("========")

