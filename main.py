import src.routing.router as router
import src.constants.screen_names as screenNames
import src.api.api as api

api.api()
router.navigate_user(screenNames.STARTUP_SCREEN)