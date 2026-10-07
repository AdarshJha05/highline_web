# Registration Funnel Implementation Plan

To move beyond the static `mailto:` interceptor, the following architecture is required to securely process admissions, collect payments, and sync data.

## Target Flow
1. **Apply:** User submits the form on `admissions.html` or a course page.
2. **Registration ID:** System generates a unique identifier (format: `HFS-YYYY-####`).
3. **Payment:** User is securely redirected to Razorpay to pay the admission or course fee.
4. **Confirmation Email:** Upon success, a branded confirmation email is sent via Resend/SendGrid.
5. **Receipt:** A branded PDF receipt is attached to the email.
6. **Data Sync:** The registration record is written to a Google Sheet for the admissions team.

## Architecture (Vercel Serverless)
Because the current stack is pure static (HTML/JS), we will introduce Vercel Serverless Functions in the `/api` directory.
- `/api/create-order` (Razorpay integration)
- `/api/verify-payment` (Razorpay webhook verification, triggers email and Sheets sync)

**Dependencies required at implementation:**
- `@razorpay/sdk`
- `googleapis` (for Sheets)
- `resend` (for emails)

*Note: Do not build this until confirmed as in-scope by the client.*
