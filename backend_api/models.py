from django.db import models
import uuid
from django.utils import timezone


class Product(models.Model):
    product_title = models.CharField(max_length=255, blank=True, null=True, default='')
    product_code = models.CharField(max_length=255, unique=True, default='')
    deposit_start_time = models.DateTimeField(blank=True, null=True)
    view_start_time = models.DateTimeField(blank=True, null=True)
    auction_start_time = models.DateTimeField(blank=True, null=True)
    auction_end_time = models.DateTimeField(blank=True, null=True)

    product_auction_status = models.IntegerField(default=0)  # 1: raw , 2: current, 3: end

    product_type = models.IntegerField(blank=True, null=True)
    product_kind = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True, default='')
    product_begin_prize = models.IntegerField(blank=True, null=True)
    product_step_prize = models.IntegerField(blank=True, null=True)
    product_loc_city = models.CharField(max_length=128, blank=True, null=True)
    product_loc_district = models.CharField(max_length=128, blank=True, null=True)
    product_loc_wards = models.CharField(max_length=128, blank=True, null=True)
    product_loc_street = models.CharField(max_length=255, blank=True, null=True)
    product_detail_data = models.TextField(blank=True, null=True)
    product_image_1 = models.FileField(upload_to='product/image/{0}'.format(uuid.uuid4()),
                                                                   blank=True, null=True)
    product_image_2 = models.FileField(upload_to='product/image/{0}'.format(uuid.uuid4()),
                                       blank=True, null=True)
    product_image_3 = models.FileField(upload_to='product/image/{0}'.format(uuid.uuid4()),
                                       blank=True, null=True)
    product_image_4 = models.FileField(upload_to='product/image/{0}'.format(uuid.uuid4()),
                                       blank=True, null=True)

    product_owner_type = models.IntegerField(blank=True, null=True)  # 1 : ca nhan , 2 : doanh nghiep
    product_owner_name = models.CharField(max_length=255, blank=True, null=True)
    product_owner_business_regis_no = models.CharField(max_length=128, blank=True, null=True)
    product_owner_business_regis_no_date = models.DateField(blank=True, null=True)
    product_owner_business_regis_no_place = models.CharField(max_length=255, blank=True, null=True)
    product_owner_tax_code = models.CharField(max_length=128, blank=True, null=True)
    product_owner_phone = models.CharField(max_length=128, blank=True, null=True)
    product_owner_email = models.CharField(max_length=128, blank=True, null=True)
    product_owner_city = models.CharField(max_length=128, blank=True, null=True)
    product_owner_district = models.CharField(max_length=128, blank=True, null=True)
    product_owner_wards = models.CharField(max_length=128, blank=True, null=True)
    product_owner_street = models.CharField(max_length=255, blank=True, null=True)
    product_owner_represent_surname = models.CharField(max_length=128, blank=True, null=True)
    product_owner_represent_name = models.CharField(max_length=128, blank=True, null=True)
    product_owner_represent_position = models.CharField(max_length=128, blank=True, null=True)
    product_owner_represent_phone = models.CharField(max_length=128, blank=True, null=True)
    product_owner_represent_email = models.CharField(max_length=128, blank=True, null=True)
    product_owner_represent_gender = models.CharField(max_length=128, blank=True, null=True)
    product_owner_represent_dob = models.DateField(blank=True, null=True)
    product_owner_represent_id_card = models.CharField(max_length=128, blank=True, null=True)
    product_owner_represent_id_card_date = models.DateField(blank=True, null=True)
    product_owner_represent_id_card_place = models.CharField(max_length=255, blank=True, null=True)
    product_owner_represent_id_card_image_front = models.FileField(upload_to='product/owner/{0}'.format(uuid.uuid4()), blank=True, null=True)
    product_owner_represent_id_card_image_back = models.FileField(upload_to='product/owner/{0}'.format(uuid.uuid4()), blank=True, null=True)
    product_owner_represent_bank_no = models.CharField(max_length=128, blank=True, null=True)
    product_owner_represent_bank_name = models.CharField(max_length=128, blank=True, null=True)
    product_owner_represent_bank_branch = models.CharField(max_length=128, blank=True, null=True)
    product_owner_represent_bank_user_name = models.CharField(max_length=128, blank=True, null=True)
    created_time = models.DateTimeField(default=timezone.now)
    modified_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.product_title
