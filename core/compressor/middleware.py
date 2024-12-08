import brotli

class BrotliMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Check if client accepts brotli compression
        if 'br' not in request.META.get('HTTP_ACCEPT_ENCODING', ''):
            return response
            
        # Don't compress if response is already compressed
        if response.has_header('Content-Encoding'):
            return response
            
        # Only compress text responses
        if not response.get('Content-Type', '').startswith(('text/', 'application/json')):
            return response
            
        # Compress content
        compressed_content = brotli.compress(response.content)
        response.content = compressed_content
        response['Content-Length'] = str(len(compressed_content))
        response['Content-Encoding'] = 'br'
        
        return response