module.exports = {
  apps: [
    {
      name: 'app',
      script: 'yarn start',

      // Options reference: https://pm2.keymetrics.io/docs/usage/application-declaration/
      instances: 1,
      autorestart: true,
      watch: true,
      env: {
        NODE_ENV: 'development',
      },
      env_production: {
        NODE_ENV: 'production',
        GRAPHQL_URI: 'https://dofuslab.io/api/graphql',
      },
    },
  ],

  deploy: {
    production: {
      key: '/home/jeremy/.ssh/id_rsa.pub',
      user: 'jeremy',
      host: '134.209.168.215',
      ref: 'origin/optimize_css',
      repo: 'git@github.com:samlee405/dofus-lab.git',
      path: '/var/www/production',
      'post-deploy':
        'cd client && yarn && yarn build && pm2 reload ecosystem.config.js --env production && pm2 save',
      env: {
        GRAPHQL_URI: 'https://dofuslab.io/api/graphql',
      },
    },
  },
};
