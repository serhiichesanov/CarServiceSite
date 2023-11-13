from .test_car import test_get_cars
from .test_car import test_create_car_s, test_create_car_f
from .test_car import test_get_car_s, test_get_car_f
from .test_car import test_update_car_by_id_s, test_update_car_by_id_f
from .test_car import test_delete_car_by_id_s, test_delete_car_by_id_f

from .test_user import test_get_users_s, test_get_users_unauthorized
from .test_user import test_create_user_s, test_create_user_f
from .test_user import test_get_user_s, test_get_user_f
from .test_user import test_get_user_uname_s, test_get_user_uname_f
from .test_user import test_update_user_by_id_s, test_update_user_by_id_f
from .test_user import test_delete_user_by_id_s, test_update_user_by_id_f
from .test_user import test_delete_user_by_id_unauthorized

from .test_admin import test_create_admin_s, test_create_admin_f
from .test_admin import test_get_admin_s, test_get_admin_f
from .test_admin import test_update_admin_s, test_update_admin_f
from .test_admin import test_delete_admin_s, test_delete_admin_f, test_get_admins

from .test_rent import test_create_rent_s, test_create_rent_f
from .test_rent import test_get_rents, test_get_rent_s, test_get_rent_f
from .test_rent import test_update_rend_f, test_update_rent_s
from .test_utils import get_last_entry
