describe("Test suite - conjunto de pruebas", ()=>  {
    
    it("Validar pagina de inicio", () => {

        cy.visit("https://zero.webappsecurity.com")
        cy.get(".active > img").should("be.visible")
        cy.get(".active > .custom > h4").contains("Online Banking")
    })

    it("Prueba E2E - transfer founds", () => {

        cy.visit("https://zero.webappsecurity.com")
        cy.get("#signin_button").click()
        

    })

    it("Validar 3", () => {


    })

})