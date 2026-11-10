from urllib.parse import urlparse
import ipaddress


def check_url(url):
    warnings = []

    try:
        parsed = urlparse(url)
        hostname = parsed.hostname or ""
    except ValueError:
        return ["Invalid URL format"]

    if "@" in url:
        warnings.append("URL contains @ symbol")

    if len(url) > 100:
        warnings.append("URL is longer than 100 characters")

    try:
        ipaddress.ip_address(hostname)
        warnings.append("URL uses an IP address")
    except ValueError:
        pass

    if len(hostname.split(".")) >= 5:
        warnings.append("URL has many hostname segments")

    if "xn--" in hostname:
        warnings.append("URL contains punycode")

    if parsed.scheme == "http":
        warnings.append("URL uses HTTP")

    return warnings


def main():
    while True:
        url = input("\nEnter URL (or q to quit): ").strip()

        if url.lower() in ("q", "quit", "exit"):
            print("Thank you for using the checker!")
            break

        if not url:
            print("Please enter a URL.")
            continue

        results = check_url(url)

        if results:
            print("\nWarnings found:")
            for warning in results:
                print("-", warning)
            print("Review carefully!")
        else:
            print("No listed warning signs found.")
            print("This does NOT prove the URL is safe.")


if __name__ == "__main__":
    main()