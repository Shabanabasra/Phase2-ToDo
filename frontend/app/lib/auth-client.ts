import { createAuthClient } from 'better-auth/client';

export const authClient = createAuthClient({
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000',
  fetch: globalThis.fetch,
});

// Export auth helpers
export const { signIn, signUp, signOut, useSession } = authClient;