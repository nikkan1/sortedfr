import vk_api


def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = False
    return key, remember_device


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password, auth_handler=auth_handler)
    try:
        vk_session.auth()
    except vk_api.AuthError as err:
        print(err)
        return
    vk = vk_session.get_api()
    resp = vk.friends.get(fields="bdate")
    if resp["items"]:
        for item in sorted(resp["items"], key=lambda val: (val["last_name"], val["first_name"])):
            if item.get("first_name", "") != "DELETED":
                print(item.get("last_name", ""), item.get(
                    "first_name", ""), item.get("bdate", ""))


if __name__ == "__main__":
    main()
