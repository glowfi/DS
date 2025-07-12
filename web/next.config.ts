import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
    /* config options here */
    env: {
        GITHUB_LINK: process.env.GITHUB_LINK,
        SITE_NAME: process.env.SITE_NAME
    }
};

export default nextConfig;
