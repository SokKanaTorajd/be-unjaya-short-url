# unjaya-short-url
URL Shortening project for UNJAYA. Initiated by Wijatama Diwangkara as DSC Lead Unjani Yogyakarta 2020

routing: .../register:
    endpoint(1) --> {
                'message': 'User has been created', 'status': 'success'
            }

routing: .../login:
    endpoint(1) --> {
                'access_token': access_token, 'token_type': 'bearer', 
                'message': 'Data is valid', 
                'status': 'success'
            }
    endpoint(0) incorrect password --> {
        detail: 'Incorrect Password'
    }
    endpoint(0) username not found --> {
        detail: 'Incorrect Username'
    }

routing: .../home:
    endpoint(1) url created  --> {
                'message': 'URL shorten has created', 
                'shorten': shorter_url, 
                'status': 'success'
            }
    endpoint(1) url updated --> {
        'status': 'success', 
        'message': 'URL shorten has updated', 
        'shorten': shorter_url
    }
    endpoint(0) --> {
        detail: 'Feature works after login'
    }

routing: .../show_url:
    endpoint(0) url not found --> {
        detail: "URL did'nt created yet"
    }
    endpoint(0) cookie not found --> {
        detail: "Cookie has expired"
    }
    endpoint(1) url show --> {
        'status': 'success', 
        'result': provide
    }

routing: .../r/url_shorten:
    endpoint(0) url createn first not found and updated not found: {
        detail: "URL is None"
    }

routing: .../logout:
    endpoint(1) --> {
        'status': 'success', 
        'message': 'You has logout'
    }
