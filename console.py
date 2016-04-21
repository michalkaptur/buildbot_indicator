from stat_checker import StatChecker

SERVER_ADDRESS = "http://buildbot.buildbot.net"
BUILDERS = ["py26-tw0900", "py26-tw1020", "py26-tw1110"]
BRANCH = "master"


checker = StatChecker(SERVER_ADDRESS, BUILDERS, BRANCH)
checker.update_builders_status()

if checker.all_builds_succedded() is False:
    print("Failed builds:")
    print(checker.get_nok_builds())
else:
    print("OK")