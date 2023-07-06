from . import main, auth, admin, prodi, predict

from functools import wraps
from flask import abort


def requires_access_level(access_level):
        def decorator(func):
            @wraps(func)
            def decorated_function(*args, **kwargs):
                # Dapatkan hak akses pengguna saat ini, misalnya dari objek pengguna yang telah diautentikasi
                user_access_level = current_user.level

                if user_access_level > access_level:
                    # Jika hak akses pengguna tidak memenuhi persyaratan, hentikan permintaan dan kembalikan respons 403 Forbidden
                    abort(403)

                # Jika hak akses pengguna memenuhi persyaratan, lanjutkan eksekusi fungsi asli
                return func(*args, **kwargs)

            return decorated_function

        return decorator