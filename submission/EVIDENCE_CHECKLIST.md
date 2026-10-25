# IBM DevOps Capstone — 33-task evidence checklist

**Important:** This starter bundle does not create genuine GitHub Actions, Kanban, Docker, Kubernetes, or Tekton evidence. Capture evidence from your own environment and replace placeholders with actual outputs. Do not submit fabricated screenshots or terminal logs.

| Task | Required evidence | Suggested location |
|---:|---|---|
| 1 | Public README URL with updated successful-build badge | GitHub README.md URL |
| 2 | Public user-story template URL | GitHub user-story.md URL |
| 3 | Kanban screenshot: stories in New Issues | planning-userstories-done.png |
| 4 | Kanban screenshot: stories under Ice Box | planning-productbacklog-done.png |
| 5 | Product backlog stories labelled Technical Debt or Enhancement | planning-labels-done.png |
| 6 | Stories estimated and assigned to Sprint 1 | planning-kanban-done.png |
| 7 | Public setup.cfg URL | GitHub setup.cfg URL |
| 8 | “Setting up the development environment” moved to Done | rest-techdebt-done.png |
| 9 | “Read an account from the service” moved to Done | read-accounts.png |
| 10 | “List all accounts in the service” moved to Done | list-accounts.png |
| 11 | “Update an account in the service” moved to Done | update-accounts.png |
| 12 | “Delete an account in the service” moved to Done | delete-accounts.png |
| 13 | Real cURL CREATE command and output | rest-create-done |
| 14 | Real cURL LIST command and output | rest-list-done |
| 15 | Real cURL READ command and output | rest-read-done |
| 16 | Real cURL UPDATE command and output | rest-update-done |
| 17 | Real cURL DELETE command and output | rest-delete-done |
| 18 | Two new stories in Sprint 2 backlog | sprint2-plan.png |
| 19 | Full successful GitHub Actions run output | ci-workflow-done |
| 20 | CI automation story moved to Done | ci-kanban-done.png |
| 21 | Public ci-build.yaml URL with checkout, lint, then nosetests | GitHub workflow URL |
| 22 | Public service/__init__.py URL showing Talisman headers | GitHub file URL |
| 23 | Actual test output for tests and CORS implementation | security-headers-done |
| 24 | Security headers/CORS story moved to Done | security-kanban-done.png |
| 25 | Three stories added to Sprint 3 | sprint3-plan.png |
| 26 | Actual API output from the internal browser on port 8080 | kube-app-output |
| 27 | Docker containerization story moved to Done | kube-docker-done.png |
| 28 | Kubernetes deployment story moved to Done | kube-kubernetes-done.png |
| 29 | Public Dockerfile URL | GitHub Dockerfile URL |
| 30 | Actual Docker image details: name, tag, ID, created time, size | kube-images |
| 31 | Actual Kubernetes deployment, pods, replica sets and service output | kube-deploy-accounts |
| 32 | Full real Tekton PipelineRun logs | pipelinerun.txt |
| 33 | CD pipeline story moved to Done after deployment | cd-pipeline-done.png |

## Screenshot capture
1. Open the actual Kanban board with the requested column/story state visible.
2. Include enough context to identify the board and columns.
3. Capture the screenshot using your OS screenshot tool and save it with the requested filename.
4. Do not submit mockups or generated screenshots as evidence.

## Command output
Copy the actual command and full output from the lab environment. Use the course's configured cluster/context for Kubernetes and Tekton; local Docker alone is not proof of a Kubernetes/Tekton run.
