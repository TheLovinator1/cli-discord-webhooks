import dhooks
import sys
import logging
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Send messages to Discord via webhooks."
    )

    parser.add_argument(
        "url",
        type=str,
        action="store",
        help="webhook url (change discordapp.com to discord.com)",
    )

    parser.add_argument(
        "message",
        type=str,
        action="store",
        help="message we are going to send",
    )

    parser.add_argument(
        "-v", "--verbose", action="store_true", help="increase output verbosity"
    )

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    if not len(sys.argv) > 1:
        print(
            "discord-webhook: missing URL and message\n"
            "Usage: discord-webhook URL MESSAGE\n\n"
            "Try 'discord-webhook --help' for more options."
        )
        sys.exit(2)

    webhook_url = args.url
    webhook_message = args.message

    logging.debug(f"Webhook url: {webhook_url}")
    logging.debug(f"Webhook message: {webhook_message}")

    hook = dhooks.Webhook(webhook_url)

    hook.send(f"{webhook_message}")