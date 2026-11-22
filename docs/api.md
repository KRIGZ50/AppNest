# API contract

Every route gets an entry here when it is finished. The frontend and the security
testing are built against this file, so keep it current.

## Template

### METHOD /path
- **Auth:** none | dashboard cookie | application secret
- **Request:** fields and where they go (JSON body / query / headers)
- **Success response:** status code and JSON shape
- **Errors:** status code and message for each error it can return
