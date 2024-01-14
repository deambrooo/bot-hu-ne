from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'BSDK kuch likh nahi to bol mat'

    elif 'hello' in lowered:
        return 'Bhonko'
    elif "teri ma choddunga bot" in lowered:
        return (
            "abe apni ma chodda he tu teri mene chod aur teri aukat nahi he meri ma ko chune ki (dont use words like that or you will got banned")
    elif 'chal dice uchal mere liye' in lowered:
        return f'ye lele dice roll apni gand me: {randint(1,6)}'