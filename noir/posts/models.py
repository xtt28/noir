"""Models for the "posts" app.

This package contains database schemas for post-related records.

Typical usage example:

    post = Post.objects.create(creator=user, content="This is some content")
    replies = post.replies
"""

from django.db import models
from users.models import NUser


class Post(models.Model):
    """A representation of a post.

    Although they are associated with a user, posts should not display the name
    of their creator.

    Attributes:
        creator: The user who created the post.
        created_at: The time at which the post was created.
        updated_at: The time at which the post was most recently updated.
        content: The textual content of the post."""

    creator = models.ForeignKey(NUser, on_delete=models.CASCADE, related_name="posts")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    content = models.TextField()


class Reply(models.Model):
    """A comment on a post.

    Replies must be associated with a post and may additionally have child
    replies.

    Attributes:
        creator: The creator of the reply.
        created_at: The time at which the reply was created.
        updated_at: The time at which the reply was most recently updated.
        post: The post that the reply is in response to.
        parent: Optional; the reply's parent reply."""

    creator = models.ForeignKey(NUser, on_delete=models.CASCADE, related_name="replies")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="replies")
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="children", null=True, blank=True
    )
