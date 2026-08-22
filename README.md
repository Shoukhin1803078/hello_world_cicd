### বর্তমান pipeline

```
Developer
   │
   │ git push main
   ▼
GitHub
   │
   ▼
GitHub Actions
   │
   ├── Checkout
   ├── Docker Build
   ├── Docker Hub Login
   └── Docker Push
   │
   ▼
Docker Hub
   │
   ▼
SSH → EC2
   │
   ├── docker pull
   ├── docker stop
   ├── docker rm
   └── docker run
```

এখানে **GitHub Actions-ই তোমার CI/CD engine** হিসেবে কাজ করছে।
