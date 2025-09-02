from django.urls import path

from .views import (
    account,
    banner,
    contact,
    content,
    gallery,
    home,
    newsletter,
)
from .views.blog import PostDetailView, PostListView
from .views.shop import shop_web, shop_webhook

app_name = "web"

urlpatterns = [
    # Home
    path("", home.home_index_view, name="home"),
    # Account
    path("account/signup/", account.account_signup_view, name="account_signup"),
    path("account/login/", account.account_login_view, name="account_login"),
    path("account/logout/", account.account_logout_view, name="account_logout"),
    path("account/profile/", account.account_profile_view, name="account_profile"),
    path("account/delete/", account.account_delete_view, name="account_delete"),
    path(
        "account/profile/update/",
        account.account_update_profile_view,
        name="account_update_profile",
    ),
    path(
        "account/avatar/update/",
        account.account_update_avatar_view,
        name="account_update_avatar",
    ),
    path(
        "account/change-password/",
        account.account_change_password_view,
        name="account_change_password",
    ),
    path(
        "account/subscriptions/",
        account.account_subscriptions_view,
        name="account_subscriptions",
    ),
    path(
        "account/subscription/cancel/<str:token>/",
        account.account_subscription_cancel_view,
        name="account_subscription_cancel",
    ),
    path("account/credits/", account.account_credits_view, name="account_credits"),
    path(
        "account/credit-purchases/",
        account.account_credit_purchases_view,
        name="account_credit_purchases",
    ),
    path(
        "account/product-purchases/",
        account.account_product_purchases_view,
        name="account_product_purchases",
    ),
    path(
        "account/signup/success",
        account.account_signup_success_view,
        name="account_signup_success",
    ),
    path(
        "account/logout/success",
        account.account_logout_success_view,
        name="account_logout_success",
    ),
    path(
        "account/password-recovery/",
        account.account_password_recovery_view,
        name="account_password_recovery",
    ),
    path(
        "account/password-recovery/success/",
        account.account_password_recovery_success_view,
        name="account_password_recovery_success",
    ),
    path(
        "account/reset-password/<uuid:token>/",
        account.account_reset_password_view,
        name="account_reset_password",
    ),
    path(
        "account/reset-password/success/",
        account.account_reset_password_success_view,
        name="account_reset_password_success",
    ),
    path(
        "account/activation/pending/",
        account.account_activation_pending_view,
        name="account_activation_pending",
    ),
    path(
        "account/activate/<uuid:token>/",
        account.account_activate_view,
        name="account_activate",
    ),
    path(
        "account/activation/success/",
        account.account_activation_success_view,
        name="account_activation_success",
    ),
    path(
        "account/address/update/",
        account.account_update_address_view,
        name="account_update_address",
    ),
    # Content
    path("c/<slug:category_tag>/", content.contents_index_view, name="contents_index"),
    path("c/i/<int:content_id>/", content.content_by_id_view, name="content_by_id"),
    path("c/t/<slug:content_tag>/", content.content_by_tag_view, name="content_by_tag"),
    # Gallery
    path("gallery/", gallery.gallery_index_view, name="gallery_index"),
    path("gallery/i/<int:gallery_id>/", gallery.gallery_by_id_view, name="gallery_by_id"),
    path("gallery/t/<slug:gallery_tag>/", gallery.gallery_by_tag_view, name="gallery_by_tag"),
    # Contact
    path("contact/", contact.contact_index_view, name="contact_index"),
    # Shop
    path("shop/plans/<str:plan_type>/", shop_web.shop_plans_view, name="shop_plans"),
    path("shop/products/", shop_web.shop_products_view, name="shop_products"),
    path(
        "shop/product/<int:product_id>/",
        shop_web.shop_product_details_view,
        name="shop_product_details_no_slug",
    ),
    path(
        "shop/product/<int:product_id>/<slug:slug>/",
        shop_web.shop_product_details_view,
        name="shop_product_details",
    ),
    path(
        "shop/checkout/<str:type>/<str:code>/",
        shop_web.shop_checkout_view,
        name="shop_checkout",
    ),
    path(
        "shop/payment/success/<str:token>/",
        shop_web.shop_payment_success_view,
        name="shop_payment_success",
    ),
    path(
        "shop/payment/error/<str:token>/",
        shop_web.shop_payment_error_view,
        name="shop_payment_error",
    ),
    path(
        "shop/payment/pending/<str:token>/",
        shop_web.shop_payment_pending_view,
        name="shop_payment_pending",
    ),
    # Shop Webhooks
    path(
        "shop/webhook/stripe/",
        shop_webhook.webhook_stripe_view,
        name="shop_webhook_stripe",
    ),
    # Banner
    path(
        "banner/track-view-access/",
        banner.track_view_access,
        name="banner_track_view_access",
    ),
    path(
        "banner/track-click-access/",
        banner.track_click_access,
        name="banner_track_click_access",
    ),
    # Newsletter
    path(
        "newsletter/subscribe/",
        newsletter.newsletter_subscribe_view,
        name="newsletter_subscribe",
    ),
    path(
        "newsletter/success/",
        newsletter.newsletter_success_view,
        name="newsletter_success",
    ),
    # Blog
    path("blog/", PostListView.as_view(), name="blog_list"),
    path("blog/<slug:slug>/", PostDetailView.as_view(), name="blog_detail"),
]
