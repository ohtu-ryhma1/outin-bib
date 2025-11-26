*** Settings ***
Library  Collections
Library  OperatingSystem
Library  BuiltIn

#AI generated
*** Keywords ***
Create Test Reference Directly
    [Arguments]  ${name}=Test dataset  ${type}=dataset  ${author}=Test Author  ${title}=Test Title  ${year}=2010  ${fields}={}
    ${ref}= Evaluate  __import__('src.services.reference_service').reference_service.create({
    ...    'name': '${name}',
    ...    'type': '${type}',
    ...    'fields': ${fields}
    ...    })  modules=src.services.reference_service
    [Return]  ${ref}

Delete All References
    ${refs}= Evaluate  __import__('src.services.reference_service').reference_service.get_all()  modules=src.services.reference_service
    :FOR  ${ref}  IN  @{refs}
    \    Evaluate  __import__('src.services.reference_service').reference_service._repo._db.session.delete(${ref})  modules=src.services.reference_service
    Evaluate  __import__('src.services.reference_service').reference_service._repo._db.session.commit()  modules=src.services.reference_service
