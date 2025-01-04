describe("Test suite - conjunto de pruebas", ()=>  {
    
    it("Validar inicio de sesión", () => {

        cy.visit("https://www.amazon.es/?tag=admarketpl0c0-21&ref=pd_sl_372417da1d68787ee8a9f55894f57c18bcb9379d0ab32ba0f7612e74")
        cy.get('#sp-cc-rejectall-link').click()
        cy.get('#nav-signin-tooltip > .nav-action-signin-button > .nav-action-inner').click()
        cy.get('#ap_email').type('bowinapou04@gmail.com')
        cy.get('.a-button-inner > #continue').click()
        cy.get('#ap_password').type('Roket132')
        cy.get('#signInSubmit').click()
        cy.get('#nav-orders').click()
        cy.get('#a-autoid-6-announce').click()
        cy.get('.a-declarative > .a-link-normal').click()
        
    })

    it("Validar las cookies", () => {

        cy.visit("https://www.amazon.es/?tag=admarketpl0c0-21&ref=pd_sl_372417da1d68787ee8a9f55894f57c18bcb9379d0ab32ba0f7612e74")
        cy.get('#sp-cc-rejectall-link').should('be.visible').then($el =>{
            if($el.length) {
                cy.wrap($el).click()
            }
        })

    })

})