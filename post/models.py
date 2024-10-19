from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import UsefulModel
from users.models import UserModel


class ProblemModel(UsefulModel):
    title = models.CharField(verbose_name=_('Title'), max_length=128)
    description = models.TextField(verbose_name=_('Description'))
    user = models.ForeignKey(UserModel, related_name='problems', on_delete=models.SET_NULL, null=True, blank=True)
    is_pinned = models.BooleanField(verbose_name=_('Is pinned'), default=False)
    total_views = models.PositiveIntegerField(default=0)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Problem")
        verbose_name_plural = _("Problems")

    @property
    def total_comments(self):
        return self.comments.count()

    @property
    def total_likes(self):
        return self.likes.user.count()


class OfferModel(UsefulModel):
    title = models.CharField(verbose_name=_('Title'), max_length=128)
    description = models.TextField(verbose_name=_('Description'))
    user = models.ForeignKey(UserModel, related_name='offers', on_delete=models.SET_NULL, null=True)
    is_pinned = models.BooleanField(verbose_name=_('Is pinned'), default=False)
    total_views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Offer")
        verbose_name_plural = _("Offers")

    @property
    def total_comments(self):
        return self.comments.count()

    @property
    def total_likes(self):
        return self.likes.user.count()


class CommentProblemModel(UsefulModel):
    comment = models.TextField(verbose_name=_("Comment"))
    user = models.ForeignKey(UserModel, related_name='problem_comments', on_delete=models.SET_NULL, null=True)
    problem = models.ForeignKey(ProblemModel, related_name='comments', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.problem.title}/{self.comment}"

    class Meta:
        verbose_name = _("Comment on Problem")
        verbose_name_plural = _("Comments on Problem")

    @property
    def total_likes(self):
        return self.likes.user.count()


class CommentOfferModel(UsefulModel):
    comment = models.TextField(verbose_name=_("Comment"))
    user = models.ForeignKey(UserModel, related_name='offer_comments', on_delete=models.SET_NULL, null=True)
    offer = models.ForeignKey(OfferModel, related_name='comments', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.offer.title}/{self.comment}"

    class Meta:
        verbose_name = _("Comment on Offer")
        verbose_name_plural = _("Comments on Offer")

    @property
    def total_likes(self):
        return self.likes.user.count()


class LikeOfferModel(models.Model):
    user = models.ManyToManyField(UserModel, related_name='like_offers')
    offer = models.OneToOneField(OfferModel, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}/{self.offer.title}"

    class Meta:
        verbose_name = _("Like Offer")
        verbose_name_plural = _("Like Offers")


class LikeProblemModel(models.Model):
    user = models.ManyToManyField(UserModel, related_name='like_problems')
    problem = models.OneToOneField(ProblemModel, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}/{self.problem.title}"

    class Meta:
        verbose_name = _("Like Problem")
        verbose_name_plural = _("Like Problems")


class LikeCommentOfferModel(models.Model):
    user = models.ManyToManyField(UserModel, related_name='like_comment_offer')
    offer_comment = models.OneToOneField(CommentOfferModel, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}/{self.offer_commnet.comment}"

    class Meta:
        verbose_name = _("Like Offer Comment")
        verbose_name_plural = _("Like Offer Comments")


class LikeCommentProblemModel(models.Model):
    user = models.ManyToManyField(UserModel, related_name='like_comment_problem')
    problem_comment = models.OneToOneField(CommentProblemModel, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}/{self.problem_comment.comment}"

    class Meta:
        verbose_name = _("Like Problem Comment")
        verbose_name_plural = _("Like Problem Comments")
