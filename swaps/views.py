from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import SwapRequest, Feedback
from django.contrib import messages
from django.db.models import Q
from .forms import FeedbackForm

# Create your views here.

@login_required
def send_swap_request(request, to_user_id):
    to_user = get_object_or_404(User, id=to_user_id)
    if request.method == 'POST':
        skill_requested = request.POST.get('skill_requested_by_sender')
        skill_offered = request.POST.get('skill_offered_by_sender')
        if skill_requested and skill_offered:
            SwapRequest.objects.create(
                from_user=request.user,
                to_user=to_user,
                skill_requested_by_sender=skill_requested,
                skill_offered_by_sender=skill_offered
            )
            messages.success(request, 'Swap request sent!')
        else:
            messages.error(request, 'Please select both skills.')
    return redirect('swap_requests')

@login_required
def swap_requests(request):
    sent = SwapRequest.objects.filter(from_user=request.user)
    received = SwapRequest.objects.filter(to_user=request.user)
    return render(request, 'swap_requests.html', {'sent': sent, 'received': received})

@login_required
def request_detail(request, pk):
    swap = get_object_or_404(SwapRequest, pk=pk)
    return render(request, 'request_detail.html', {'swap': swap})

@login_required
def accept_swap(request, pk):
    swap = get_object_or_404(SwapRequest, pk=pk, to_user=request.user)
    swap.status = 'Accepted'
    swap.save()
    messages.success(request, 'Swap request accepted.')
    return redirect('swap_requests')

@login_required
def reject_swap(request, pk):
    swap = get_object_or_404(SwapRequest, pk=pk, to_user=request.user)
    swap.status = 'Rejected'
    swap.save()
    messages.success(request, 'Swap request rejected.')
    return redirect('swap_requests')

@login_required
def delete_swap(request, pk):
    swap = get_object_or_404(SwapRequest, pk=pk)
    if swap.from_user == request.user or swap.to_user == request.user:
        swap.delete()
        messages.success(request, 'Swap request deleted.')
    return redirect('swap_requests')

@login_required
def leave_feedback(request, pk):
    swap = get_object_or_404(SwapRequest, pk=pk)
    if swap.status != 'Accepted' or (request.user != swap.from_user and request.user != swap.to_user):
        messages.error(request, 'You cannot leave feedback for this swap.')
        return redirect('swap_requests')
    if hasattr(swap, 'feedback'):
        messages.info(request, 'Feedback already submitted.')
        return redirect('request_detail', pk=pk)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.swap_request = swap
            feedback.save()
            messages.success(request, 'Feedback submitted!')
            return redirect('request_detail', pk=pk)
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form, 'swap': swap})
