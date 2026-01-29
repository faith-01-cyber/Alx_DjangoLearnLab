# HTTPS and Security Configuration

This Django project enforces HTTPS and secure communication using Django security settings.

## Implemented Measures

- SECURE_SSL_REDIRECT redirects all HTTP traffic to HTTPS
- SECURE_HSTS_SECONDS enforces HTTPS for one year
- SECURE_HSTS_INCLUDE_SUBDOMAINS applies HSTS to subdomains
- SECURE_HSTS_PRELOAD enables browser preload
- SESSION_COOKIE_SECURE ensures session cookies use HTTPS
- CSRF_COOKIE_SECURE ensures CSRF cookies use HTTPS
- X_FRAME_OPTIONS prevents clickjacking
- SECURE_CONTENT_TYPE_NOSNIFF prevents MIME sniffing
- SECURE_BROWSER_XSS_FILTER enables XSS protection

These settings follow Django production security best practices.
