docker rm ait-test
docker run -ti --net=host -e HTTPS_PROXY=http://127.0.0.1:8888 -e HTTP_PROXY=http://127.0.0.1:8888 -e ALL_PROXY=http://127.0.0.1:8888 --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --device=/dev/kfd --device=/dev/dri --group-add video --ipc=host --shm-size 8G -e HSA_OVERRIDE_GFX_VERSION=11.0.0 -e HIP_VISIBLE_DEVICES=0 --name ait-test ait:latest
