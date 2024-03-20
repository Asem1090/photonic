from stegano import lsb


def lsb_hide(image_path, secret_message: str) -> bool:
    try:
        lsb.hide(image_path, secret_message).save(image_path)
        return True
    except:
        return False


def lsb_reveal(image_path) -> str:
    return lsb.reveal(image_path)
