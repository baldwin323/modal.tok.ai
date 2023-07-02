```python
from ContentSchema import ContentSchema

def organize_content(creator_id, content_id, category):
    content = ContentSchema.objects(content_id=content_id, creator_id=creator_id).first()
    if not content:
        return {"error": "Content not found"}

    content.category = category
    content.save()

    return {"message": "Content organized successfully"}

def create_playlist(creator_id, playlist_name, content_ids):
    playlist = {
        "creator_id": creator_id,
        "name": playlist_name,
        "content_ids": content_ids
    }

    # Assuming we have a PlaylistSchema
    new_playlist = PlaylistSchema(**playlist)
    new_playlist.save()

    return {"message": "Playlist created successfully"}
```