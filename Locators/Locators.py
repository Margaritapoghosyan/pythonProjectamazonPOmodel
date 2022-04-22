from selenium.webdriver.common.by import By

class LocatorsClass():
    #LogIn Page Locator
    LoginPageLoginFieldLocator =(By.NAME, "email")
    LoginPageContinueButtonLocator =(By.ID,"continue")

    #password Page Locator
    passwordPagePasswordFieldLocator = (By.NAME, "password")
    passwordPageSignInButtonLocator = (By.ID,"signInSubmit")

    #search field locator
    NavBarsearchFildLocator = (By.ID, "twotabsearchtextbox")

    #search Keep me signed in button locator
    KeepMeSigned = (By.NAME, "rememberMe")

    #select an element locator
    selectItem =(By.XPATH, "(//img[@class ='s-image'][1])")

    # add to cart button locator
    addToCart = (By.ID, "add-to-cart-button")

    # close button from add list locator
    closeButton = (By.XPATH, "//a[@id = 'attach-close_sideSheet-link']")

    #press cart button locator
    #cartButt = (By.XPATH, "//form[@id ='attach-view-cart-button-form']")
    cartButton = (By.XPATH,"//div[@id = 'nav-cart-text-container']")

    #delete item from cart locator
    delItem = (By.XPATH, "//input[@value ='Delete']")


    #accountAndList locator
    accountAndList = (By.XPATH,"//a[@id ='nav-link-accountList']")

    #Recommendation's locator
    recommendation = (By.LINK_TEXT, "Recommendations")

    #select element from recommendations locator
    selectedElement =(By.XPATH,"//div[@id= 'p13n-asin-index-2']")

    #open product locator
    openProduct = (By.XPATH, "//div[@id='expansion-2']/div/div/div[2]/div[2]/div[1]/a/span/div")


    #add to wish list locator
    addToWishList =(By.ID, "add-to-wishlist-button-submit")

    #signOut button locator
    signOutButton = (By.LINK_TEXT, "Sign Out")





