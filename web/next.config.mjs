/** @type {import('next').NextConfig} */
const nextConfig = {
    env: {
        GITHUB_LINK: process.env.GITHUB_LINK,
        SITE_NAME: process.env.SITE_NAME
    }
};

export default nextConfig;
