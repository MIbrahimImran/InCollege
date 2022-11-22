import src.constants.screen_names as screenNames

import src.screens.startup_screen as startupScreen
import src.screens.login_screen as loginScreen
import src.screens.signup_screen as signupScreen
import src.screens.logged_in.job_search_screen as jobsearchScreen
import src.screens.promotional_video_screen as promotionalvideoScreen
import src.screens.find_contact_screen as findcontactScreen

import src.screens.useful_links.useful_links_screen as usefulLinksScreen
import src.screens.useful_links.browse_incollege_screen as browseInCollegeScreen
import src.screens.useful_links.bussiness_solutions_screen as bussinessSolutionScreen
import src.screens.useful_links.directories_screen as directoriesScreen

import src.screens.useful_links.general.general_screen as generalScreen
import src.screens.useful_links.general.about_screen as aboutScreen
import src.screens.useful_links.general.blog_screen as blogScreen
import src.screens.useful_links.general.careers_screen as careerScreen
import src.screens.useful_links.general.developers_screen as developersScreen
import src.screens.useful_links.general.help_center_screen as helpcenterScreen
import src.screens.useful_links.general.press_screen as pressScreen

import src.screens.learn_new_skill.learn_new_skill_screen as learnnewskillScreen
import src.screens.learn_new_skill.coding_screen as codingScreen
import src.screens.learn_new_skill.communication_screen as communicationScreen
import src.screens.learn_new_skill.microsoft_excel_screen as microsoftexcelScreen
import src.screens.learn_new_skill.web_development_screen as webdevelopmentScreen
import src.screens.learn_new_skill.resume_critique_screen as resumecritiqueScreen

import src.screens.incollege_important_links.incollege_important_links_screen as importantlinksScreen
import src.screens.incollege_important_links.accessibility_screen as accessibilityScreen
import src.screens.incollege_important_links.brand_policy_screen as brandpolicyScreen
import src.screens.incollege_important_links.cookie_policy_screen as cookiepolicyScreen
import src.screens.incollege_important_links.copyright_notice_screen as copyrightnoticeScreen
import src.screens.incollege_important_links.cookie_policy_screen as copyrightpolicyScreen
import src.screens.incollege_important_links.guest_controls_screen as guestcontrollsScreen
import src.screens.incollege_important_links.languages_screen as languageScreen
import src.screens.incollege_important_links.privacy_policy_screen as privacypolicyScreen
import src.screens.incollege_important_links.user_agreement_screen as useragreementScreen

import src.screens.logged_in.show_my_network_screen as showmynetworkScreen
import src.screens.logged_in.user_home_screen as userhomeScreen
import src.screens.logged_in.current_friends_screen as currentfriendsScreen
import src.screens.logged_in.find_friends_screen as findfriendsScreen
import src.screens.logged_in.user_profile_screen as userprofileScreen
import src.screens.logged_in.pending_friend_requests_screen as pendingrequestsScreen
import src.screens.logged_in.inbox_screen as inboxScreen

# Key: ScreenName Str  Value: Screenfunction of every screen
screen_functions = {
    screenNames.STARTUP_SCREEN: startupScreen.screen,
    screenNames.LOGIN_SCREEN: loginScreen.screen,
    screenNames.SIGNUP_SCREEN: signupScreen.screen,
    screenNames.JOB_SEARCH_SCREEN: jobsearchScreen.screen,
    screenNames.USER_HOME_SCREEN: userhomeScreen.screen,
    screenNames.USEFUL_LINKS_SCREEN: usefulLinksScreen.screen,
    screenNames.BROWSE_INCOLLEGE_SCREEN: browseInCollegeScreen.screen,
    screenNames.BUSSINESS_SOLUTIONS_SCREEN: bussinessSolutionScreen.screen,
    screenNames.DIRECTORIES_SCREEN: directoriesScreen.screen,
    screenNames.GENERAL_SCREEN: generalScreen.screen,
    screenNames.ABOUT_SCREEN: aboutScreen.screen,
    screenNames.BLOG_SCREEN: blogScreen.screen,
    screenNames.CAREERS_SCREEN: careerScreen.screen,
    screenNames.DEVELOPERS_SCREEN: developersScreen.screen,
    screenNames.HELP_CENTER_SCREEN: helpcenterScreen.screen,
    screenNames.PRESS_SCREEN: pressScreen.screen,
    screenNames.LEARN_NEW_SKILL_SCREEN: learnnewskillScreen.screen,
    screenNames.CODING_SCREEN: codingScreen.screen,
    screenNames.COMMUNICATION_SCREEN: communicationScreen.screen,
    screenNames.MICROSOFT_EXCEL_SCREEN: microsoftexcelScreen.screen,
    screenNames.WEB_DEVELOPMENT_SCREEN: webdevelopmentScreen.screen,
    screenNames.RESUME_CRITIQUE_SCREEN: resumecritiqueScreen.screen,
    screenNames.INCOLLEGE_IMPORTANT_LINKS_SCREEN: importantlinksScreen.screen,
    screenNames.ACCESSIBILITY_SCREEN: accessibilityScreen.screen,
    screenNames.BRAND_POLICY_SCREEN: brandpolicyScreen.screen,
    screenNames.COOKIE_POLICY_SCREEN: cookiepolicyScreen.screen,
    screenNames.COPYRIGHT_NOTICE_SCREEN: copyrightnoticeScreen.screen,
    screenNames.COPYRIGHT_POLICY_SCREEN: copyrightpolicyScreen.screen,
    screenNames.GUEST_CONTROLS_SCREEN: guestcontrollsScreen.screen,
    screenNames.LANGUAGE_SCREEN: languageScreen.screen,
    screenNames.PRIVACY_POLICY_SCREEN: privacypolicyScreen.screen,
    screenNames.USER_AGREEMENT_SCREEN: useragreementScreen.screen,
    screenNames.PROMOTIONAL_VIDEO_SCREEN: promotionalvideoScreen.screen,
    screenNames.FIND_CONTACT_SCREEN: findcontactScreen.screen,
    screenNames.SHOW_MY_NETWORK_SCREEN: showmynetworkScreen.screen,
    screenNames.PENDING_FRIEND_REQUEST_SCREEN: pendingrequestsScreen.screen,
    screenNames.FIND_FRIENDS_SCREEN: findfriendsScreen.screen,
    screenNames.CURRENT_FRIENDS_SCREEN: currentfriendsScreen.screen,
    screenNames.USER_PROFILE_SCREEN: userprofileScreen.screen,
    screenNames.INBOX_SCREEN: inboxScreen.screen,
}
