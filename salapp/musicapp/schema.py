import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType

from .models import Artist


class ArtistName(DjangoObjectType):
    class Meta:
        model = Artist
        # fields = ('artist', 'album', 'track_name','logo_url')


class Query(graphene.ObjectType):
    artists = graphene.List(
        ArtistName,
        first=graphene.Int(),
        search=graphene.String() # Unimplemented
    )

    # Use them to slice the Django queryset
    def resolve_artists(self, info, search=None, first=None, **kwargs):
        qs = Artist.objects.all()

        if search:
            filter = (
                    Q(artist__icontainsa=search) |
                    Q(album__icontains=search) |
                    Q(track_name__icontains=search)
            )
            qs = qs.filter(filter)

        if first:
            qs = qs[:first]

        return qs

    # def resolve_artists(self, info, **kwargs):
    #     return Artist.objects.all()

# Allows user addition through mutation.
# class CreateArtist(graphene.Mutation):
#     id = graphene.Int()
#     track_name = graphene.String()
#     album = graphene.String()
#     artist = graphene.String()
#
#     #2
#     class Arguments:
#         track_name = graphene.String()
#         album = graphene.String()
#         artist = graphene.String()
#
#     #3
#     def mutate(self, track_name, album, artist):
#         artist = Artist(track_name=track_name, album=album, artist=artist)
#         artist.save()
#
#         return CreateArtist(
#             id=Artist.id,
#             track_name=Artist.track_name,
#             album=Artist.album,
#             artist=Artist.artist,
#
#         )
#
#
# #4
# class Mutation(graphene.ObjectType):
#     create_artist = CreateArtist.Field()
