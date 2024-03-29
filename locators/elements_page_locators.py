from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME = (By.CSS_SELECTOR, "input#userName")
    EMAIL = (By.CSS_SELECTOR, "input#userEmail")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea#currentAddress")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea#permanentAddress")
    SUBMIT = (By.CSS_SELECTOR, "button#submit")

    OUTPUT_FULL_NAME = (By.CSS_SELECTOR, "p#name")
    OUTPUT_EMAIL = (By.CSS_SELECTOR, "p#email")
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, "p#currentAddress")
    OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "p#permanentAddress")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Expand all']")
    CHECKBOXES_LIST = (By.CSS_SELECTOR, "span.rct-title")
    CHECK_STATUS_BOXES = (By.CSS_SELECTOR, "svg.rct-icon-check")
    CHECKBOX_TITLE = ".//ancestor::span[@class='rct-text']"
    # ancestor -- "Выбирает предков текущего узла" // CSS - div:has(> .test)
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span.text-success")
    LABEL = "label span.rct-title"


class RadioButtonPageLocators:
    YES_RADIOBUTTON = (By.CSS_SELECTOR, "label[class='custom-control-label'][for='yesRadio']")
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, "label[class=custom-control-label][for=impressiveRadio]")
    NO_RADIOBUTTON = (By.CSS_SELECTOR, "label[class=custom-control-label][for=noRadio]")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span.text-success")


class WebTablePageLocators:
    # add new person
    ADD_BUTTON = (By.CSS_SELECTOR, "button#addNewRecordButton")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "input#firstName")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "input#lastName")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input#userEmail")
    AGE_INPUT = (By.CSS_SELECTOR, "input#age")
    SALARY_INPUT = (By.CSS_SELECTOR, "input#salary")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input#department")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button#submit")

    # whole table with persons
    PERSON_LINE_IN_LIST = (By.CSS_SELECTOR, "div.rt-tr-group")
    SEARCH_BOX_INPUT = (By.CSS_SELECTOR, "input#searchBox")
    DELETE_BTN = (By.CSS_SELECTOR, "span[title=Delete]")
    # ROW_PARENT = (By.CSS_SELECTOR, "div.rt-tbody")
    ROW_LINES_ALL = (By.CSS_SELECTOR, "div.rt-tr-group")
    ROW_LINE_IN = (By.CSS_SELECTOR, "div[class$=-odd]")

    # update person info
    UPDATE_BTN = (By.CSS_SELECTOR, "span[title=Edit]")
    AGE_FIELD_INPUT = (By.CSS_SELECTOR, "input#age")
    EMAIL_FIELD_INPUT = (By.CSS_SELECTOR, "input#userEmail")
    SUBMIT_BTN_UPDATE = (By.CSS_SELECTOR, "button[type=submit]")

    # del person info
    DELETE_PERSON_INFO_BTN = (By.CSS_SELECTOR, "span[title=Delete]")
    NO_ROWS_DATA = (By.CSS_SELECTOR, "div.rt-noData")
    ROW_PER_PAGE_BTN = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')


class ButtonsPageLocators:
    DOUBLE_CLICK_BTN = (By.CSS_SELECTOR, "button#doubleClickBtn")
    RIGHT_CLICK_BTN = (By.CSS_SELECTOR, "button#rightClickBtn")
    # ORDINARY_CLICK_BTN = (By.CSS_SELECTOR, "div[class='mt-4']:nth-child(3n)")
    ORDINARY_CLICK_BTN = (By.XPATH, "//div[3]/button")

    SUCCESS_DOUBLE = (By.CSS_SELECTOR, " p#doubleClickMessage")
    SUCCESS_RIGHT = (By.CSS_SELECTOR, " p#rightClickMessage")
    SUCCESS_CLICK_ME = (By.CSS_SELECTOR, "p#dynamicClickMessage")


class LinksPageLocators:
    HOME_LINK = (By.CSS_SELECTOR, "a#simpleLink")
    BAD_REQUEST_LINK = (By.CSS_SELECTOR, "a#bad-request")


class UploadAndDownloadLocators:
    UPLOAD_FILE = (By.CSS_SELECTOR, "input[type=file]")
    UPLOADED_RESULT = (By.CSS_SELECTOR, "p#uploadedFilePath")
    DOWNLOAD_FILE = (By.CSS_SELECTOR, "a[id=downloadButton]")


class DynamicPropertiesLocators:
    WILL_ENABLE_BTN = (By.CSS_SELECTOR, "button#enableAfter")
    COLOR_CHANGE_BTN = (By.CSS_SELECTOR, "button#colorChange")
    VISIBLE_AFTER_5_SEC_BTN = (By.CSS_SELECTOR, "button#visibleAfter")
