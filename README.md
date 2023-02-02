# Tags Cog for Leek<br>[![GitHub Actions][actions-img]][actions-url] [![Patreon][patreon-img]][patreon-url] [![PayPal][paypal-img]][paypal-url] [![Discord][discord-img]][discord-url]

> WARNING: Please note that Leek is an experimental work in progress project, and as such, the API might change unexpectedly at any time.

This is an extension for adding Tags to Leek.

Tags are little snippets of text that can be created by staff members and retrieved by anyone.

## Download

* [GitHub Releases](https://github.com/LeekByLemon/LeekTags/releases)
* [GitHub Actions](https://github.com/LeekByLemon/LeekTags/actions) (experimental versions)

## Installation

Run the following command to install the latest version of Tags Extension from master.

```
pip install https://github.com/LeekByLemon/LeekTags/archive/master.zip
```

If you want to install from git for developent purposes, run the following commands:

```
git clone https://github.com/LeekByLemon/LeekTags.git leek
cd leek
pip install -e .
```

## Usage

> WARNING: Please note that the Tags require SQL support to be enabled

To add the cog to Leek, add the Cog `leek_tags:Tags` to your `DISCORD_COGS` environment variable in your `.env` file.

The next time you start the Bot, the Tag system will be available for anyone in any server. You can control the permissions in each server by going to your `Server Settings > Apps > Integrations > Your Bot Name > Manage` and changing them there.  

[actions-img]: https://img.shields.io/github/actions/workflow/status/LeekByLemon/LeekTags/main.yml?branch=master&label=actions
[actions-url]: https://github.com/LeekByLemon/LeekTags/actions
[patreon-img]: https://img.shields.io/badge/support-patreon-FF424D.svg
[patreon-url]: https://www.patreon.com/lemonchan
[paypal-img]: https://img.shields.io/badge/support-paypal-0079C1.svg
[paypal-url]: https://paypal.me/justalemon
[discord-img]: https://img.shields.io/badge/discord-join-7289DA.svg
[discord-url]: https://discord.gg/Cf6sspj
