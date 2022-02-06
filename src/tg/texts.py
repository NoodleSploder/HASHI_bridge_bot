start = "Welcome to the HASHI bridge bot, built for Polkaswap.\n" \
        "Create a notice for an ETH gas price that suits your bridging budget and the bot will send you a message" \
        " when it is less than the set price.\n" \
        "NOTE: it is recommended to always use /fast ETH gas price to avoid any bridging issues.\n" \
        "Use /info to see information.\n" \
        "Use /help for instructions"

help = '/eth - get current gas prices for bridging ETH\n' \
       '/fast, /average, /slow - create new notice. Example: "/fast 50"\n' \
       '/my_notices - manage existing notices'

info = 'NOTE: This bot uses gas estimates, please check tx before signing it.\n\n' \
       'Developed for Polkaswap.io\n' \
       'Data from etherscan.io/gastracker\n' \
       'Discussion: t.me/polkaswap\n'

donate = 'If you find this bot useful then please help by donating to the address below:\n' \
         'XOR: cnWUwYCoHEFrqmwGJEd5fg5mGXudZSsfeCF1r8LNooXf1iFZW'

ticker = 'Select below to see current bridging gas prices:\n' \
         '/eth \n' \
         '/xor \n' \
         '/pswap \n' \
         '/val \n' \
         '/ceres \n' \
         '/dai \n' \
         '/usdc \n' \


eth = '`ETH price:  {} USD\n\n' \
     'Estimated Cost of Bridging ETH\n' \
     'Tx Speed   Gwei    To      From\n' \
     'Fast:       {}    ${}     ${}\n' \
     'Average:    {}    ${}     ${}\n' \
     'Slow:       {}    ${}     ${}`\n'



dai = '`ETH price:  {} USD\n\n' \
     'Estimated Cost of Bridging DAI\n' \
     'Tx Speed   Gwei    To      From\n' \
     'Fast:       {}    ${}     ${}\n' \
     'Average:    {}    ${}     ${}\n' \
     'Slow:       {}    ${}     ${}`\n'

xor = '`ETH price:  {} USD\n\n' \
     'Estimated Cost of Bridging XOR\n' \
     'Tx Speed   Gwei    To      From\n' \
     'Fast:       {}    ${}     ${}\n' \
     'Average:    {}    ${}     ${}\n' \
     'Slow:       {}    ${}     ${}`\n'

pswap = '`ETH price:  {} USD\n\n' \
     'Estimated Cost of Bridging PSWAP\n' \
     'Tx Speed   Gwei    To      From\n' \
     'Fast:       {}    ${}     ${}\n' \
     'Average:    {}    ${}     ${}\n' \
     'Slow:       {}    ${}     ${}`\n'

val = '`ETH price:  {} USD\n\n' \
     'Estimated Cost of Bridging VAL\n' \
     'Tx Speed   Gwei    To      From\n' \
     'Fast:       {}    ${}     ${}\n' \
     'Average:    {}    ${}     ${}\n' \
     'Slow:       {}    ${}     ${}`\n'

ceres = '`ETH price:  {} USD\n\n' \
     'Estimated Cost of Bridging CERES\n' \
     'Tx Speed   Gwei    To      From\n' \
     'Fast:       {}    ${}     ${}\n' \
     'Average:    {}    ${}     ${}\n' \
     'Slow:       {}    ${}     ${}`\n'

usdc = '`ETH price:  {} USD\n\n' \
     'Estimated Cost of Bridging USDC\n' \
     'Tx Speed   Gwei    To      From\n' \
     'Fast:       {}    ${}     ${}\n' \
     'Average:    {}    ${}     ${}\n' \
     'Slow:       {}    ${}     ${}`\n'